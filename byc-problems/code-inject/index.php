<?php
 <h2>Ping a device</h2>

                <form name=\"ping\" action=\"#\" method=\"post\">
                        <p>
                                Enter an IP address:
                                <input type=\"text\" name=\"ip\" size=\"30\">
                                <input type=\"submit\" name=\"Submit\" value=\"Submit\">
                        </p>\n";

if( $vulnerabilityFile == 'impossible.php' )
        $page[ 'body' ] .= "                    " . tokenField();

$page[ 'body' ] .= "
                </form>
                {$html}
?>
