#include <stdio.h>
#include <stdlib.h>

#include "http.h"

/*
./http_test www.thomas-bayer.com restnames/countries.groovy
Response:
HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Content-Type: application/xml;charset=ISO-8859-1
Date: Wed, 25 Aug 2021 01:22:21 GMT
Connection: close
Content-Length: 6273

<?xml version="1.0" ?><restnames>
  <countries>
    <country href="http://www.thomas-bayer.com:80/restnames/namesincountry.groovy?country=Great+Britain">Great Britain</country>
    <country href="http://www.thomas-bayer.com:80/restnames/namesincountry.groovy?country=Ireland">Ireland</country>
    <country href="http://www.thomas-bayer.com:80/restnames/namesincountry.groovy?country=U.S.A.">U.S.A.</country>
    <country href="http://www.thomas-bayer.com:80/restnames/namesincountry.groovy?country=France">France</country>
	...
*/

int main(int argc, char **argv) {

    if (argc != 3) {
        fprintf(stderr, "usage: ./http_test host page\n");
        exit(1);
    }

    Buffer *response = http_query(argv[1], argv[2], 80);
    if (response) {
        printf("Response:\n%s\n", response->data);


        char *content = http_get_content(response);

        printf("Content:\n%s\n", content);
    }

    free(response);
    return 0;
}
