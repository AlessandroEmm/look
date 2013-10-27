<html>
<head>
<title> Presentee </title>
<link href='http://fonts.googleapis.com/css?family=Patua+One' rel='stylesheet' type='text/css'>
<link href='/static/main.css' rel='stylesheet' type='text/css'>

<script type="text/javascript" src="/static/js/jquery.js"></script>
<script type="text/javascript"src="/static/js/chooser.js">> </script>

</head>
<body>
<div id="container">
<div style="padding-top: 250px;"></div>
<div style="width:400px; margin-left: auto; margin-right: auto;">
<span class="title"> Presentee </span><span class="title-line" >- </span> <span class="title" >Menu</span><br />
<b style="color:grey;">Choose your Channel and Properties:</b>
<p style="margin-top:20px"> 
<span class="subtitles">Quality Mode:</span>
<br />
<a class="Quality" id="fullQuality" href="#selected"> Full </a>    <span class="subtitles">|</span>  <a class="Quality" id="limitedQuality"> Limited </a>
<br />
<br />
<span class="subtitles">Choose your channel:</span> <br />
<div class="styled-select">

<select id="selecting">
$channelList
</select>

</div>
<br />
<button class="gbutton" name="Go" aria-label="Go" id="Go"><span id="gbutton">Go!</span></button>
</p>



</div>
<div id="footer-spacer"></div>
</div>
<div id="footer" style="padding-top:7px">
<div style="width:400px; margin-left: auto; margin-right: auto;">
<a id="footertext"href="/admin"> Admin Console </a>
</div></div>

</body>
</html>
