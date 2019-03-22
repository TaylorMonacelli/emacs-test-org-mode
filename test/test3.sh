mkdir -p test3

cd test3

cat <<'__eot__' >test3.org
* one

#+PROPERTY: header-args :tangle one.sh
:PROPERTIES:
:header-args: :tangle one.sh
:END:

#+BEGIN_SRC sh
echo one
#+END_SRC

* two

#+PROPERTY: header-args :tangle two.sh
:PROPERTIES:
:header-args: :tangle two.sh
:END:

#+BEGIN_SRC sh
echo two
#+END_SRC
__eot__

emacs --batch \
	  --eval '(setq load-path (cons (expand-file-name "~/org/lisp") load-path))' \
	  -l ~/org/lisp/org \
	  --eval '(org-babel-tangle-file "test3.org")'
