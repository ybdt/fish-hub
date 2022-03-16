<?php
class YBDT {
    public $test = "123";

    function __wakeup() {
        echo "Code here was execute in __wakeup()";
        echo "<br/>";
    }

    function __construct() {
        echo "Code here was execute in __construct()";
        echo "<br/>";
    }

    function __destruct() {
        echo "Code here was execute in __destruct()";
        echo "<br/>";
    }
}
$ybdt = new YBDT();
$serialized_obj = serialize($ybdt);
print_r($serialized_obj);