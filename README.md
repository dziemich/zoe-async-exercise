# Image to emoji inferrer with gRPC

Disclaimer: it's not a very good one


We have a device equipped with camera that's sending the images it acquires to our server using gRPC which analyses the image and returns the most likely prediction of what it determines to be present on the image as emoji. 

## V0
<details>
<summary>Spec</summary>
<br>
Let's assume our camera takes a single image and sends that image to our server. A server then responds with a single prediction as well. 
</details>


## V1
<details>
<summary>Spec</summary>
<br>
Let's assume our camera streams the images as it acquires them, without any delays. The server should also process the incoming images as they come and stream back the predictions. 
</details>
