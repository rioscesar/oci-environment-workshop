//LEFT COLUMN
function getInsuredDetails(insured) {
return `
 <div class="container" style="margin-top: 3%;">

          

            <button class="collapsible" id="insuredName"><b> <svg class="svg-inline--fa fa-minus-square fa-w-14" aria-hidden="true" data-prefix="far" data-icon="minus-square" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="currentColor" d="M108 284c-6.6 0-12-5.4-12-12v-32c0-6.6 5.4-12 12-12h232c6.6 0 12 5.4 12 12v32c0 6.6-5.4 12-12 12H108zM448 80v352c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V80c0-26.5 21.5-48 48-48h352c26.5 0 48 21.5 48 48zm-48 346V86c0-3.3-2.7-6-6-6H54c-3.3 0-6 2.7-6 6v340c0 3.3 2.7 6 6 6h340c3.3 0 6-2.7 6-6z"></path></svg><!-- <i class="far fa-minus-square"></i> --> &nbsp; &nbsp; </b><p>Name: ${insured.name} </p></button>
            <div class="content">
                <br>
                <div>
                    

                    <div class="row">
                        <div class="col-md-4">
                            <p style="text-align: left; ">
                                <div id="leftColumn"></div>
                        
                            </p>
                        </div>
                        <div class="col-md-4">
                            <p style="text-align: left; ">
                            <div id="middleColumn"><br> Address: ${insured.address} <br> Phone: ${insured.phone} <br> SSN: ${insured.ssn} <br> Type: Property and Casualties</div>

                       
                            </p>
                        </div>
                        <div class="col-md-4">
                            <p style="text-align: left; ">
                       <div id="rightColumn"></div>

                            
                            </p>
                        </div>
                    </div>

                


                </div>
                <br>
                <br>
            </div>
   
            
        </div>

`;


}
function showInsured(getInsuredDetails) {
        document.querySelector("#duplicate").innerHTML += getInsuredDetails;
}


window.onload = function soap() {
    var data = 'localhost';
    var xmlhttp = new XMLHttpRequest();  
    xmlhttp.open('POST', 'http://'+data+':8001/LibertyInsurance-WebServiceApp-context-root/HelloWorldAppPort?wsdl', true);

    // build SOAP request
    var sr =
        '<?xml version="1.0" encoding="UTF-8"?>'+
        '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'+
            '<soap:Header/>'+
            '<soap:Body>'+
                '<ns1:getFromDB xmlns:ns1="http://webserviceapp/"/>'+
            '<\/soap:Body>'+
        '<\/soap:Envelope>';
    
    // Send the POST request
    xmlhttp.setRequestHeader('Content-Type', 'text/xml');
    xmlhttp.setRequestHeader('SOAPAction', 'getFromDB');
    xmlhttp.send(sr);
    // send request
    
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {
            if (xmlhttp.status == 200) {
                var xmlDoc = $.parseXML( xmlhttp.responseText ),
                $xml = $(xmlDoc),
                $value= $xml.find("return");
                var arr = [];
                for (var i = 0; i < $value.length; i++) {
                    arr.push($value[i].textContent);
                }
                var customers = '['+arr.join(', ')+']';
                console.log(customers);
                console.log(JSON.parse(customers));
                
                JSON.parse(customers).map(getInsuredDetails).forEach(showInsured);
                var coll = document.getElementsByClassName("collapsible");
                var i;
        
                for (i = 0; i < coll.length; i++) {
                    coll[i].addEventListener("click", function() {
                        this.classList.toggle("active");
                        var content = this.nextElementSibling;
                        if (content.style.display === "block") {
                            content.style.display = "none";
                        } else {
                            content.style.display = "block";
                        }
                    });
                }
            }
        }
    }
}





