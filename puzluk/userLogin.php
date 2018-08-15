<?php
	session_start();
	session_regenerate_id();
		
	$sessionID = session_id();
	echo $sessionID;
	
	$servername = "localhost";
	$server_username = "root";
	$server_password = "";
	$dbName = "puzluk_db";
	
	//Make connection
	$conn = new mysqli($servername, $server_username, $server_password, $dbName);
	
	//Check connection
	if(!$conn){
		die("Connection Failed. " . mysqli_connect_error());
	}
	
	//$avatar = "Megatron";
	//$_SESSION["Avatar"] = "Giggity";
	$_SESSION["Avatar"] = $_POST["avatarPost"];
	
	if(isset($_SESSION["Avatar"])){

		//storing avatar
		//$_SESSION["Avatar"] = $avatar;

		$sql = "SELECT avatar FROM users WHERE avatar = '".$_SESSION["Avatar"]."'";
		$result = mysqli_query($conn, $sql);
		
		// Getting a result and confirming login
		if(mysqli_num_rows($result) > 0){
			//Show data for each row
			while($row = mysqli_fetch_assoc($result)){
				if($row['avatar'] == $_SESSION["Avatar"]){
					echo "Correct User Access! " .$row['avatar'];
				}else{
					echo "No Such User, Type Correct Avatar Name or Create New User!";
				}
			}
		}else{
			echo "User Not Found";
		}
		
		mysqli_close($conn);
	}
?>