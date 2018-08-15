<?php
	$servername = "localhost";
	$server_username = "root";
	$server_password = "";
	$dbName = "puzluk_db";
	
	$username = $_POST["usernamePost"];
	$password = $_POST["passwordPost"];
	
	//Make connection
	
	$conn = new mysqli($servername, $server_username, $server_password, $dbName);
	
	//Check connection
	
	if(!$conn){
		die("Connection Failed. " . mysqli_connect_error());
	}
	
	$sql = "SELECT password FROM admin_user WHERE username = '".$username."'";
	$result = mysqli_query($conn, $sql);
	
	// Getting a result and confirming login
	if(mysqli_num_rows($result) > 0){
		//Show data for each row
		while($row = mysqli_fetch_assoc($result)){
			if($row['password'] == $password){
				echo "Login Success!";
			}else{
				echo "Password Incorrect, Login Failed!";
			}
		}
	}else{
		echo "User Not Found";
	}
?>