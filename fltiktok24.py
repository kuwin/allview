ban = f"""                        .-/+osssso+/-`\n                   `/sdNMMMMMMMMMMMMMMNds/`\n                .odMMMMMMMMMMMMMMMMMMMMMMMMdo.\n              :hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh:\n            -dMMMNmMMMMMMMNNNNNNNNNNMMMMMMMmNMMMd-\n          `sMNNs-oMMMMNNNNNNNNNNNNNNNNNNMMMMo-sNNMs\n         `dM+s-:sMMMNNNNNNMMNMNNMNMMNNNNNNMMMs-:s+Md`\n        `mho.h/:dMNNMMMNMMNmNoso-dmNMMNMMMNNMd:/d`ohm`\n        hs//::oMMNMMMMNMMMMNMmmo+NNMMMMNMMMMNMNo:-+:yh\n       /M--y+:hMNNNNNNNMMMNNMMmmMMNMMMMNNNNNNNMh:oy.:M:\n       dd+./.hMNMMMMMNMMMNNNNNooNNNNNMMMNMMMMMNMy./.odh\n      `M-m-/yyMNMMMMMNMMMMNMNdssdNMNMMMMNMMMMMNMyy/-m-N\n      `M:-ho`NMNNNNNNNNNmho-sN:/Ms-shmNNNNNNNNNMm`sh-/M`\n      `Mh`+ sdMNMMMMMh`     NMosMN     `dMMMMMNMdo`/`hN\n       d/h/.m.MNMMMMM+      yM--My      oMMMMMNM.m`/h/h\n       /d`/ss mNNNNNN-      `d.-h`      -NNNNNNd ss/`d:\n        hm/`+ d:mNMMN                    NMMNd:h`+`/mh\n        `doss/++.mNNh                    hNNm`o//ssod`\n         `ds.:+y-:sso                    osy:-y+--sd`\n           sMy+/:./+                      +/.:/+yMs\n            -dyo/////.```            ```./////ohh-\n              :hMhoosss/`            `/sssoohMh:\n                .ohysoos.            .soosyh+`\n                   `/sdN`            `Nds/`\n\n   ...:::: Telegram: mhttps://t.me/nhomspamcallsms ::::...                  
"""
for i in ban:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.00)

username=input('Nhập Username Tik Tok ( Không Nhập @ ): ')
while True:
    headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6','cache-control': 'max-age=0','priority': 'u=0, i','sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'cross-site','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',}
    access=requests.get('https://tikfollowers.com/free-tiktok-followers', headers=headers)
    try:
        session=access.cookies['ci_session']
        headers.update({'cookie': f'ci_session={session}'})
        token=access.text.split("csrf_token = '")[1].split("'")[0]
        data='{"type":"follow","q":"@'+username+'","google_token":"t","token":"'+token+'"}'
        search=requests.post('https://tikfollowers.com/api/free', headers=headers, data=data).json()
        if search['success']==True:
            data_follow=search['data']
            data='{"google_token":"t","token":"'+token+'","data":"'+data_follow+'","type":"follow"}'
            send_follow=requests.post('https://tikfollowers.com/api/free/send', headers=headers, data=data).json()
            if send_follow['o']=='Success!' and send_follow['success']==True and send_follow['type']=='success':
                print('Tăng Follow Tik Tok Thành Công')
                continue
            elif send_follow['o']=='Oops...' and send_follow['success']==False and send_follow['type']=='info':
                try:
                    thoigian=send_follow['message'].split('You need to wait for a new transaction. : ')[1].split('.')[0]
                    phut=thoigian.split(' Minutes')[0]
                    giay=int(phut)*0
                    for i in range(giay, 0, -1):
                        print(f'Vui Lòng Chờ {i} Giây...', end='\r')
                        time.sleep(1)
                    continue
                except:
                    print('Lỗi Không Xác Định               ')
                    continue
    except:
        print('Lỗi Không Xác Định               ')
        continue
