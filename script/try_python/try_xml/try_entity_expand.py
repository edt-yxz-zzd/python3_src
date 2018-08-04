xml = '''<?xml version="1.0"?>
<!DOCTYPE root [
    <!ELEMENT p (#PCDATA)>
    <!ENTITY try "&#60;">
        <!-- replacement txt == str"<"
            if put &try into content, will create a begin of tag
        -->
    <!ENTITY try2 "&#38;#60;">
        <!-- == lt
            replacement txt == str"&#60;" since &#38; included
        -->
    <!ENTITY e0 "&amp;lt;&try2;&#38;#38;lt;">
        <!-- only char_ref/peref included, i.e. &#38 -> '&'
             &amp; and &try2 are bypassed
            [ref"&amp;", str"lt;", ref"&try2;", str"&#38;lt;"]
            replacement txt == "&#38;lt&#60;&#38;lt;"
        -->
    <!ENTITY e1 "e0&e0;">
        <!-- bypassed, so treat "&#38;" as text
            ==>> "e0&#38;lt&#60;&#38;lt"
        -->
    <!ENTITY e2 "e1&e1;">
    <!ENTITY e3 "e2&e2;">
    <!ENTITY e4 "e3&e3;">

    <!ENTITY e6 "&amp;lt;">
    <!ENTITY e7 "">
    <!ENTITY % pe0 ""><!-- quot;&#59;&#38;apos;" - ->
    <!ENTITY e5 "pe0%pe0;"> -->
]>
<root>
    <p>
        &#60;&lt;&try2;
        <!-- &try; can place here!-->

        &e0;
            <!--
                str"&#38;lt;&#60;&#38;lt;"
                included in content;
                    like C "#include"
                    require further recognize
                recognized as ==>> "&lt;<&lt;"
            -->
        &e1;
        &e2;
        &e3;
        &e4;

         e5;
    </p>
</root>
'''

#    <!ENTITY % pe0 "e3&e3;&lt;&#38;lt;"> error when pe0 used in e5
#    <!ENTITY % pe0 "e3&e3;&59;&#38;38;"> -- not well-fromed  '<' from e3

import xml.etree.ElementTree as E

t = E.fromstring(xml)
txt = t[0].text
print(txt)
print(repr(txt))

assert (txt ==
    '\n        &lt;<<\n        e0&lt;<<\n        e1e0&lt;<<\n        e2e1e0&lt;<<\n       e3e2e1e0&lt;<<\n    ')


