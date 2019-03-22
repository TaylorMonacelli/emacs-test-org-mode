mkdir -p test5

cd test5

cat <<'__eot__' >test5.org
* l1 header

#+PROPERTY: :tangle one.sh
:PROPERTIES:
:header-args: :tangle one.sh
:END:

** l2 header

#+BEGIN_SRC sh
echo one
#+END_SRC

* l1 header

#+PROPERTY: :tangle two.sh
:PROPERTIES:
:header-args: :tangle two.sh
:END:

** l2 header

#+BEGIN_SRC sh
echo two
#+END_SRC
__eot__

emacs --batch \
	  --eval '(setq load-path (cons (expand-file-name "~/org/lisp") load-path))' \
	  -l ~/org/lisp/org \
	  --eval '(org-babel-tangle-file "test5.org")'
