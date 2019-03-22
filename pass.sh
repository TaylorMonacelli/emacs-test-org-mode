set -e

docker build -t emacs-org-test .
docker rm -f emtest 2>/dev/null || true
docker run --rm -h emtest --name emtest -it emacs-org-test bash -c '\
cd ~/org; \
git clean -dfx; \
git checkout "57d8b68d9594d4e23d5f4960073a1cac78bc72e3~1"; \
make autoloads; \
cd /tmp/test; \
rm -rf /tmp/test/test1/{two,one}.sh; \
make test'
