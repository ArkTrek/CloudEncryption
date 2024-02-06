// Google sign-in success callback function
function onSignIn(googleUser) {
    // Retrieve Google user credentials
    const profile = googleUser.getBasicProfile();
    const idToken = googleUser.getAuthResponse().id_token;

    // Authenticate with Firebase using Google OAuth token
    const credential = firebase.auth.GoogleAuthProvider.credential(idToken);
    firebase.auth().signInWithCredential(credential)
        .then((userCredential) => {
            // User signed in successfully
            const user = userCredential.user;
            console.log('User signed in:', user.displayName);
            // Redirect or perform any other action after successful sign-in
        })
        .catch((error) => {
            // Handle errors
            console.error('Error signing in:', error);
        });
}
