#!/bin/bash
# displays only the status code of the response.
curl -s -w "%{http_code}" "$1"
