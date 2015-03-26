# cms-forest

A repository which contains several CMS versions to aid with the testing of droopescan.

All files not matching the regexes present on clean_non_static.sh will be periodically deleted.

Url files in the format droopescan expects are in urls/. Example usage:

<pre>
./droopescan scan drupal -U /var/www/html/urls/drupal.txt -e v
</pre>
