mkdir -p test1

cd test1

cat <<'__eot__' >test1.org
* l1 header

** l2 header

#+PROPERTY: header-args :tangle one.sh
:PROPERTIES:
:header-args: :tangle one.sh
:header-args: :results output silent
:header-args: :comments link
:header-args: :padline no
:END:

#+BEGIN_SRC sh
echo one
#+END_SRC

** l2 header
#+PROPERTY: header-args :tangle two.sh
:PROPERTIES:
:header-args: :tangle two.sh
:header-args: :results output silent
:header-args: :comments link
:header-args: :padline no
:END:

#+BEGIN_SRC sh
echo two
#+END_SRC
__eot__

emacs --batch \
	  --eval '(setq load-path (cons (expand-file-name "~/org/lisp") load-path))' \
	  -l ~/org/lisp/org \
	  --eval '(org-babel-tangle-file "test1.org")'
