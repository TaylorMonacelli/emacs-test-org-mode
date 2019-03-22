test: /usr/local/bin/bats
	$(MAKE) clean
	./run.sh
	bats *.bats

/usr/local/bin/bats:
	./install_bats.sh

clean:
	@find . -maxdepth 1 -type d -name 'test*' | xargs rm -rf
	@rm -f *.bats
