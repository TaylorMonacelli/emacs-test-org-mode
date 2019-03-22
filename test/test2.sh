mkdir -p test2

cd test2

cat <<'__eot__' >test2.org
* one

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

* two

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
	  --eval '(org-babel-tangle-file "test2.org")'
