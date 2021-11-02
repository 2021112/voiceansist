# coding=utf-8
import turing
import baiduApi


if __name__ == "__main__":
    api_id = "25095095"
    api_key = "4BG3o3240KG45bRLDCnYa2EX"
    api_secert = "DGX9P8IhFZsnYRmCn7gOmgzO32yowNGC"
    bdr = baiduApi.BaiduRest(api_id, api_key, api_secert)
    while True:
        input("按下回车开始说话，自动停止")
        print('开始录音')
        bdr.recorder("output.wav")
        print("结束")
        ask = bdr.getText('output.wav')
        print('你：', ask)
        robot = turing.Turing()
        ans = robot.anser(ask)
        print('机器人：', ans)
        bdr.speak2(ans)
        # bdr.getVoice(ans, "output.mp3")
        # bdr.speakMac("output.mp3")
