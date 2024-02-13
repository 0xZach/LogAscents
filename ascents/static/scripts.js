function redirect_to_ascent(pk){
    document.location.href="ascent_details/"+pk+"/"; 
    // TODO: using django's url system doesn't seem to work,
    // and this looks like a security fault
    // so better try to find how to make it work
}