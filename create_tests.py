#!/usr/bin/env python

import os
import pathlib

import yaml
from jinja2 import Template

documents = """
---
contents: |
 * Heading1
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 ** Subheading1
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

 #+BEGIN_SRC sh
 echo sub-one
 #+END_SRC

 * Heading2
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :END:

 #+BEGIN_SRC sh
 echo two
 #+END_SRC

 ** Subheading2
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :END:

 #+BEGIN_SRC sh
 echo sub-two
 #+END_SRC
---
contents: |
 * Heading1
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 ** Subheading1

 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

  #+BEGIN_SRC sh
  echo two
  #+END_SRC

 * Heading1
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 ** Subheading2
 :PROPERTIES:
 :header-args:clojure:    :session *clojure-2*
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC
---
contents: |
 * Heading1
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 ** Subheading1
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

  #+BEGIN_SRC sh
  echo two
  #+END_SRC

 * Heading1
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 ** Subheading2
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC
---
contents: |
 * Heading1
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

  #+BEGIN_SRC sh
  echo one
  #+END_SRC

 ** Subheading1
 :PROPERTIES:
 :header-args:clojure:    :session *clojure-2*
 :END:

 #+BEGIN_SRC sh
 echo two
 #+END_SRC

 * Heading1
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :header-args:clojure:    :session *clojure-1*
 :header-args:R:          :session *R*
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 ** Subheading2
 :PROPERTIES:
 :header-args:clojure:    :session *clojure-2*
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC
---
contents: |
 * top
 ** one
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 ** two
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :END:

 #+BEGIN_SRC sh
 echo two
 #+END_SRC
---
contents: |
 * l1 header

 ** l2 header
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :header-args: :results output silent
 :header-args: :comments link
 :header-args: :padline no
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 ** l2 header
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :header-args: :results output silent
 :header-args: :comments link
 :header-args: :padline no
 :END:

 #+BEGIN_SRC sh
 echo two
 #+END_SRC
 ---
contents: |
 * one
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :header-args: :results output silent
 :header-args: :comments link
 :header-args: :padline no
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 * two
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :header-args: :results output silent
 :header-args: :comments link
 :header-args: :padline no
 :END:

 #+BEGIN_SRC sh
 echo two
 #+END_SRC
---
contents: |
 * one
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 * two
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :END:

 #+BEGIN_SRC sh
 echo two
 #+END_SRC
---
contents: |
 * top
 ** one
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 ** two
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :END:

 #+BEGIN_SRC sh
 echo two
 #+END_SRC
---
contents: |
 * l1 header
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_one.sh
 :END:

 ** l2 header

 #+BEGIN_SRC sh
 echo one
 #+END_SRC

 * l1 header
 :PROPERTIES:
 :header-args: :tangle {{ basename }}_two.sh
 :END:

 ** l2 header

 #+BEGIN_SRC sh
 echo two
 #+END_SRC
"""

tpl_bats = Template("""{# jinja2 -#}
@test "{{ basename }}" {

    emacs --batch \\
    	  --eval '(setq load-path (cons (expand-file-name "~/org/lisp") load-path))' \\
    	  --load ~/org/lisp/org \\
    	  --eval '(org-babel-tangle-file "{{ basename }}.org")'

    result="$(ls {{ basename }}*.sh | wc -l)"
    [ "$result" -eq 2 ]
}
""")

org_dcts = list(yaml.load_all(documents))

for index, dct in enumerate(org_dcts, 1):
    basename = 'scratch_test{}'.format(index)
    orgfile = '{}.org'.format(basename)
    batsfile = "{}.bats".format(basename)
    tpl_str = dct['contents']
    tpl = Template(tpl_str)

    with open(orgfile, 'w') as file_h:
        file_h.write(tpl.render(
            {**dct, 'basename': basename}))

    with open(batsfile, 'w') as file_h:
        file_h.write(tpl_bats.render(
            {'basename': basename}))
