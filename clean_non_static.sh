#!/bin/bash

function delete_non_static() {
    files=`find * -type f | grep -vE '\.(js|css|txt|xml|sql|json|yml|sh|md)$'`
    for file in $files; do rm $file; done
}

function delete_vendor() {
    files=`find * -type f | grep vendor`
    for file in $files; do rm $file; done;
}

delete_non_static
delete_vendor
