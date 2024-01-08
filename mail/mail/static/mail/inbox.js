

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
  console.log("am working load")
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
  const emailsView = document.querySelector('#emails-view');
  const compose = document.querySelector('#compose-view');
  const recipients = document.querySelector('#compose-recipients');
  const subject =  document.querySelector('#compose-subject');
  const body = document.querySelector('#compose-body');

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  document.querySelector('#compose-form').onsubmit = send_email;
  // By default, load the inbox
  load_mailbox('inbox');


});

