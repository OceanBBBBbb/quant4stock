# 导入futu-api
import futu as ft

# 实例化行情上下文对象
quote_ctx = ft.OpenQuoteContext(host="10.0.30.140", port=11111)

# 上下文控制
quote_ctx.start()              # 开启异步数据接收
quote_ctx.set_handler(ft.TickerHandlerBase())  # 设置用于异步处理数据的回调对象(可派生支持自定义)

# 低频数据接口
market = ft.Market.HK
code = 'HK.00123'
code_list = [code]
plate = 'HK.BK1107'
print(quote_ctx.get_trading_days(market, start=None, end=None))   # 获取交易日
print(quote_ctx.get_stock_basicinfo(market, stock_type=ft.SecurityType.STOCK))   # 获取股票信息
print(quote_ctx.get_autype_list(code_list))                                  # 获取复权因子
print(quote_ctx.get_market_snapshot(code_list))                              # 获取市场快照
print(quote_ctx.get_plate_list(market, ft.Plate.ALL))                         # 获取板块集合下的子板块列表
print(quote_ctx.get_plate_stock(plate))                         # 获取板块下的股票列表

# 高频数据接口
quote_ctx.subscribe(code, [ft.SubType.QUOTE, ft.SubType.TICKER, ft.SubType.K_DAY, ft.SubType.ORDER_BOOK, ft.SubType.RT_DATA, ft.SubType.BROKER])
print("这是报价信息返回：")
price_list = quote_ctx.get_stock_quote(code)
print(price_list)  # 获取报价
print(price_list[1].last_price)  # 获取报价
# print(quote_ctx.get_rt_ticker(code))   # 获取逐笔
# print(quote_ctx.get_cur_kline(code, num=100, ktype=ft.KLType.K_DAY))   #获取当前K线
# print(quote_ctx.get_order_book(code))       # 获取摆盘
# print(quote_ctx.get_rt_data(code))          # 获取分时数据
# print(quote_ctx.get_broker_queue(code))     # 获取经纪队列
#
# # 停止异步数据接收
# quote_ctx.stop()
#
# # 关闭对象
# quote_ctx.close()
#
# # 实例化港股交易上下文对象
# trade_hk_ctx = ft.OpenHKTradeContext(host="127.0.0.1", port=11111)
#
# # 交易接口列表
# print(trade_hk_ctx.unlock_trade(password='123456'))                # 解锁接口
# print(trade_hk_ctx.accinfo_query(trd_env=ft.TrdEnv.SIMULATE))      # 查询账户信息
# print(trade_hk_ctx.place_order(price=1.1, qty=2000, code=code, trd_side=ft.TrdSide.BUY, order_type=ft.OrderType.NORMAL, trd_env=ft.TrdEnv.SIMULATE))  # 下单接口
# print(trade_hk_ctx.order_list_query(trd_env=ft.TrdEnv.SIMULATE))      # 查询订单列表
# print(trade_hk_ctx.position_list_query(trd_env=ft.TrdEnv.SIMULATE))    # 查询持仓列表

# trade_hk_ctx.close()