document.addEventListener('DOMContentLoaded', (event) => {

  let sender = document.querySelector('input[name="sender"]').value

  console.log(sender)
  let formattedSenderNum = sender.replace(/(\d{1})(\d{3})(\d{3})(\d{4})/, '+$1 ($2) $3-$4')

  console.log(formattedSenderNum)

  document.querySelector('input[name="sender"]').value = formattedSenderNum
});
