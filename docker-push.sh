#!/usr/bin/env bash
docker build -t base -f Dockerfile.base .
docker tag base bookpark/base
docker push bookpark/base
