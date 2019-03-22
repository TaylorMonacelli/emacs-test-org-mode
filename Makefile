all:
	$(MAKE) setup
	docker run --rm --name emtest -it emacs-org-test bash -c 'cd /tmp/test && bash all.sh'
	$(MAKE) clean

setup:
	$(MAKE) files

	docker build -t emacs-org-test .
	docker rm -f emtest 2>/dev/null || true

files:
	@python create_tests.py

clean:
	@rm -f scratch_*
