.PHONY: check ci
check:
	python3 tests/check_sm90_ulp.py

ci:
	python3 tests/check_sm90_ulp.py --strict-ci
