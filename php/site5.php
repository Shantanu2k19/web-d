<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>

    <!-- including php and html page for this website-->
    <body>
        <?php 
            $title = "php learning";
            $author = "shan";
            $wordcount = "400";

            include "header.php";
            
            sayhi($author);
        ?>

        <p>the in-between text for the page </p>

        <?php include "footer.html" ?>
    </body>
</html>