<?php
	// Variables for server connection
	$servername = "localhost";
	$server_username = "root";
	$server_password = "";
	$dbName = "puzluk_db";
	
	// Variables for the Admin users
	$username = $_POST["usernamePost"];  //"BenTest";
	$email = $_POST["emailPost"];  //"test email";
	$password = $_POST["passwordPost"]; //"12345";
	
	//Make connection
	
	$conn = new mysqli($servername, $server_username, $server_password, $dbName);
	
	//Check connection
	
	if(!$conn){
		die("Connection Failed. " . mysqli_connect_error());
	}
	
	$sql = "INSERT INTO admin_user (username, email, password)
			VALUES ('".$username."','".$email."','".$password."')";
	$result = mysqli_query($conn, $sql);
	
	if(!$result){
		echo "There was an error";
	}else{
		echo "User Created. Everything OK";
	}
?>