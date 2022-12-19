from flask import Flask
import backend

app = Flask(__name__)

## Webhook Listener
@app.route('/webhook_listener', methods=['POST'])
def webhook_listener():
    serials = backend.get_mv_serials(backend.net_id)
    print(serials)
    if len(serials) == 1:
        current_status = backend.mv_current_audio_status(serials[0])

        if current_status == False:
            backend.mv_enable_audio(serials[0])
        elif current_status == True:
            backend.mv_disable_audio(serials[0])
    if len(serials) > 1:
        for i in serials:
            count = 0
            current_status = backend.mv_current_audio_status(i[count])
            if current_status == False:
                backend.mv_enable_audio(i[count])
                count = count + 1
            elif current_status == True:
                backend.mv_disable_audio(i[count])
                count = count + 1
    return "success", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
