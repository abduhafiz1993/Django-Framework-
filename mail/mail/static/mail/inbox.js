

function compose_email() {

  // Show compose view and hide other views
  emailsView.style.display = 'none';
  compose.style.display = 'block';

  // Clear out composition fields
  recipients.value = '';
  subject.value = '';
  body.value = '';
}

function email_view(id){

  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {

    console.log(email);

    emailsView.style.display = 'none';
    compose.style.display = 'none';
    detail.style.display = 'block';

    detail.innerHTML = `
    <ul class="list-group">
      <li class="list-group-item"><strong>From:</strong> ${email.sender}</li>
      <li class="list-group-item"><strong>To:</strong> ${email.recipients}</li>
      <li class="list-group-item"><strong>Subject:</strong> ${email.subject}</li>
      <li class="list-group-item"><strong>Timestamp:</strong> ${email.timestamp}</li>
      <li class="list-group-item">${email.body}</li>
    </ul>
    `

    // Change to read
    if(!email.read) {
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
          read: true
        })
      })
    }

    const btn_arch = document.createElement('button');
    btn_arch.innerHTML = email.archived ? "Unarchive" : "Archive";
    btn_arch.addEventListener('click', function() {
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: !email.archived
        })
      })
      .then(() => {load_mailbox('archive')})
    });
    detail.append(btn_arch);


    // Reply logic
    const btn_reply = document.createElement('button');
    btn_reply.innerHTML = "Reply"
    btn_reply.addEventListener('click', function() {
      compose_email();

      document.querySelector('#compose-recipients').value = email.sender;
      let subject = email.subject;
      if(subject.split(' ', 1)[0] != "Re:") {
        subject = "Re: " + email.subject;
      }
      document.querySelector('#compose-subject').value = subject;
      document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote: ${email.body}`;
    });
    detail.append(btn_reply);
  });
}

  

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  emailsView.style.display = 'block';
  detail.style.display = 'none';
  compose.style.display = 'none';

  // Show the mailbox name
  emailsView.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Print emails
    console.log(emails);

    emails.forEach(singleEmail=>{
      console.log(singleEmail);

      const element = document.createElement('div');
      element.className = "list-group-item"
      element.innerHTML = `
        <h6>From: ${singleEmail.sender}</h6>
        <h5>Subject: ${singleEmail.subject}</h5>
        <p>${singleEmail.timestamp}</p>
      `;

      singleEmail.className = singleEmail.read ? 'read': 'unread';
      
      element.onclick = () => {
        email_view(singleEmail.id)
      };

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
  detail = document.querySelector('#detail')

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  document.querySelector('#compose-form').onsubmit = send_email;
  // By default, load the inbox
  load_mailbox('inbox');


});

