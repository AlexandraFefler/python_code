import nexmo

client = nexmo.Client(key='906554d2', secret='uK8kJk72LtW8326E')

client.send_message({
    'from': 'Vonage APIs',
    'to': '972522236749',
    'text': 'El. Psy. Congroo.',
})