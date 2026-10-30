**Activity 2**

Abstract class media  
	Protected title  
	Protected file size

	Constructor (title, size)  
		This.title \= title  
		This.size \= size  
End of class

Class video inherits from media  
	Private resolution

	Constructor (title, size, resolution )  
		Media constructor(title,size)  
		This.resolution \= resolution  
End of class

Class audio inherits from media  
	Private sample rate  
	  
	constructor (title, size, sample rate)  
	Media constructor (title, size)  
	This.sample rate \= sample rate   
End of class

**Activity 3**

// add an abstract method to the the abstract media class as well as the video and audio classes

Abstract class media

Protected…  
.  
.

constructor(...)  
.  
.  
.

	Abstract method play()

End of class

Class video inherits from media 

	Private…  
	  
	constructor(...)  
	.  
	.  
	.  
	  
	Override method play()  
		Print ‘playing video at quality’  
End of class

Class audio inherits from media

	Private… 

	constructor(...)  
	.  
	.  
	.

	Override method play()  
		Print ‘playing audio at sample rate’  
	

