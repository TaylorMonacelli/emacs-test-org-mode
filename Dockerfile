FROM silex/emacs:latest

RUN apt-get -qqy update
RUN apt-get -qqy install make git
RUN git clone https://github.com/sstephenson/bats.git /usr/local/src/bats && cd /usr/local/src/bats && ./install.sh /usr/local
RUN git clone https://code.orgmode.org/bzg/org-mode.git ~/org
RUN mkdir -p /tmp/test
COPY scratch_test* *.sh /tmp/test/
RUN rm -f /tmp/test/scratch*{two,one}.sh


