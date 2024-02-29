function search_bar(){
    document.location.href="{% url 'list' query="+document.getElementById("search_bar").value+" %}";
}