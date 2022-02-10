function addMore(){

    
    document.getElementById('error').innerHTML=" ";
        let name = document.getElementById('name').value;
        if(name==''){
            document.getElementById('error').innerHTML="Please enter value !";
        }
        else{
            var newtodo =  document.getElementById('list');
            var paragraph = document.createElement('li');
            paragraph.classList.add('paragraph-styling');
            paragraph.textContent = name;
            newtodo.appendChild(paragraph);
        }
         
        document.getElementById('name').value=" ";

        paragraph.addEventListener('click', function(){
            paragraph.style.textDecoration = "line-through"

            paragraph.addEventListener('dblclick', function(){
                list.removeChild(paragraph);
            })
        }
        )
        
    
    }

    
    








