<html>
	<head>
		<title>PWNME Login</title>
		<link rel="stylesheet" type="text/css" href="bootstrap.min.css">
	</head>
	<body>
	  <nav class="navbar navbar-default" role="navigation">
	    <div class="container-fluid">
	      <!-- Brand and toggle get grouped for better mobile display -->
	      <div class="navbar-header">
		 <img src="dolla.png" style="height: 80px"><span style="margin-left: 10px; font-size: 19px;line-height: 21px;height: 60px;">Public Wealth Negotiation Mega-Enterprise
	      </div>

	    </div><!-- /.container-fluid -->
	  </nav>
    <div class="container">
	  <div class="row">
	    <div class="col-md-12">
	<?php 
	      if (!isset($_COOKIE["session_id"])) {
	      	      setcookie("session_id", "67", time()+3600);	 
		      echo "<h3>Welcome!</h3> <p>This is your first time here, so were assigning you a new session number.</p> <p>Your session number is <b>67</b>.</p><p>We'll be tracking you using this number whenever you visit this site.</p>";
	      }
	      else {
	      	   echo "<h3>Welcome Back!</h3><p>Your session number is <b>" . intval($_COOKIE["session_id"]) . "</b>.</p><p>We'll be tracking you using this number whenever you visit this site.</p>"; 
	      }
       	?>
	<?php
	      $logged_in = isset($_COOKIE["session_id"]) && intval($_COOKIE["session_id"]) > 20 && intval($_COOKIE["session_id"]) < 67;
	      $expired = isset($_COOKIE["session_id"]) && intval($_COOKIE["session_id"]) < 66;
	      if ($logged_in) {
		 echo "You're in! FLAG: there_is_no_cookie";
	      }
	      elseif ($expired) {
	      	 echo "<span style='color: red;'>Your login session has expired. You will need to log in again.</span>";
	      }
	      else {
	      	 echo "There are currently too many users logged in, so you will have to come back later to log in.";
	      }
	?>
	 </div>
	 </div>
</div>
	</body>
</html>
