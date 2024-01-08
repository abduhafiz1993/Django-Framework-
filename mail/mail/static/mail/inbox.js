

function compose_email() {

  // Show compose view and hide other views
  emailsView.style.display = 'none';
  compose.style.display = 'block';

  // Clear out composition fields
  recipients.value = '';
  subject.value = '';
  body.value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  emailsView.style.display = 'block';
  compose.style.display = 'none';

  // Show the mailbox name
  emailsView.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Print emails
    console.log(emails);

    emails.forEach(singleEmail=>{
      compose_email.log(singleEmail);

      const element = document.createElement('div');
      element.className = "list-group-item"
      element.innerHTML = `
        <h6>Sender: ${singleEmail.sender}</h6>
        <h5>Subject: ${singleEmail.subject}</h5>
        <p>${singleEmail.timestamp}</p>
      `;

      singleEmail.className = singleEmail.read ? 'read': 'unread';
      element.addEventListener('click', function() {
        console.log('This element has been clicked!')
      });
      emailsView.append(element);

    })



    // ... do something else with emails ...
  });
}


function send_email(){
  const recipientsValue = recipients.value;
  const subjectValue = subject.value;
  const bodyValue = subject.body;

  fetch('/emails', {
    method:'POST',
    body:JSON.stringify({
      recipients:recipientsValue,
      subject:subjectValue,
      body: bodyValue
    })
  })
  .then(response => response.json())
  .then(result => {
    console.log(result)
    load_mailbox('sent');
  });
  return false
}

document.addEventListener('DOMContentLoaded', function() {

  // varibales
  emailsView = document.querySelector('#emails-view');
  compose = document.querySelector('#compose-view');
  recipients = document.querySelector('#compose-recipients');
  subject =  document.querySelector('#compose-subject');
  body = document.querySelector('#compose-body');

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  document.querySelector('#compose-form').onsubmit = send_email;
  // By default, load the inbox
  load_mailbox('inbox');


});

