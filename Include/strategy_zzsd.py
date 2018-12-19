# 一个简单的追涨杀跌策略
import time
import futu as ft

list=[]
quote_ctx = ft.OpenQuoteContext(host="10.0.30.140", port=11111)
code='US.AAPL'  # 选择标的
LENGTH=12 # 样本容量
quote_ctx.subscribe(code, [ft.SubType.QUOTE, ft.SubType.TICKER, ft.SubType.K_DAY, ft.SubType.ORDER_BOOK, ft.SubType.RT_DATA, ft.SubType.BROKER])
# 实例化美股交易上下文对象
trade_us_ctx = ft.OpenUSTradeContext(host="10.0.30.140", port=11111)
trade_us_ctx.unlock_trade(password='123456')

def doTicker():
    print("开始执行追涨杀跌策略购买AAPL")
    last = quote_ctx.get_stock_quote(code) #获取最新报价
    last_price = last[1].last_price
    if len(list) < LENGTH:
        list.append(last_price) #累加最近（=逐笔）
    else:
        pMax = max(list) # 取出最高价
        pMin = min(list) # 取出最低价
        if last_price > pMax: # 最新价是周期内的新高(追涨)
            account = trade_us_ctx.accinfo_query(trd_env=ft.TrdEnv.SIMULATE)
            print("buy " + str(account))
            if account[1].power > last_price: # 资产足够(买1股)
                trade_us_ctx.place_order(price=last_price, qty=1, code=code, trd_side=ft.TrdSide.BUY,
                                         order_type=ft.OrderType.NORMAL, trd_env=ft.TrdEnv.SIMULATE)  # 下单接口
        elif last_price < pMin:
            account = trade_us_ctx.accinfo_query(trd_env=ft.TrdEnv.SIMULATE)
            print("sell " + str(account))
            if account[1].Stocks > 0:
                trade_us_ctx.place_order(price=last_price, qty=1, code=code, trd_side=ft.TrdSide.SELL,
                                              order_type=ft.OrderType.NORMAL, trd_env=ft.TrdEnv.SIMULATE)  # 下单接口
        list.pop(0)
        list.append(last_price)
    print("当前的list" + str(list))

if __name__=="__main__":
    while 1:
        doTicker() #执行策略
        time.sleep(30) #休息一段时间 30s

