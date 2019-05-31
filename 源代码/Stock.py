#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class stock(object):
    def __init__(self):
        self.goods = []

    def add(self, product):
        """
        添加新产品：
        如果有新产品，直接添加到原有库存中。
        不是新产品则添加数量。
        """
        # goods中有库存
        if len(self.goods) > 0:
            flag = 0
            for i in range(len(self.goods)):
                if (self.goods[i].index == product.index):
                    self.goods[i].number += product.number
                    flag = 1
                    break
            if (flag == 0):
                self.goods.append(product)
        # goods中无库存
        else:
            self.goods.append(product)

    def dele(self,data,mount):
        """
        取出产品产品：
            库存中有产品：
                产品数量小于所需数量：
                    输出提示--库存不够，只有多少数量
                产品数大于或等于所需数量：
                    减少库存，并输出提示--剩余库存数量
            库存中没有产品：
                输出提示--没有产品
        """
        text=''
        flag = 0
        index=0
        name=''
        if data.isdigit():
            index=eval(data)
        else:
            name=data

        # for j in self.goods:
        #     if j.index==index:
        #         product = j
        for i in range(len(self.goods)):
            if (self.goods[i].index == index or self.goods[i].name == name):
                flag = 1
                product=self.goods[i]
                if (self.goods[i].number >= mount):
                    self.goods[i].number -= mount
                    text+=('产品ID：%s | 产品名称：%s | 产品剩余数量：%s | 产品价格：%s\n' % (
                    self.goods[i].index, self.goods[i].name, self.goods[i].number, self.goods[i].price))
                if (self.goods[i].number < mount):
                    text +=('产品ID：%s | 产品名称：%s | 产品数量：%s | 产品价格：%s\n' % (
                    self.goods[i].index, self.goods[i].name, self.goods[i].number, self.goods[i].price))
                    text +=("库存数量不足！！\n")
                elif(product.number<=5):
                    text+=("注意，库存数量少于5件\n")
                break
        if (flag == 0):
            text +=("库存中没有该产品！！\n")
        return text

    def List(self, l):
        """
        查找产品：
            库存中有产品：
                输出产品详情
            库存中没有产品：
                输出提示--没有产品
        """
        flag = 0
        if (isinstance(l, int)):
            for i in range(len(self.goods)):
                if (self.goods[i].index == l):
                    flag = 1
                    print('产品ID：%s | 产品名称：%s | 产品数量：%s | 产品价格：%s' % (
                    self.goods[i].index, self.goods[i].name, self.goods[i].number, self.goods[i].price))
            if (flag == 0):
                print("库存中没有该产品！！")

        else:
            for i in range(len(self.goods)):
                if (self.goods[i].name == l):
                    flag = 1
                    print('产品ID：%s | 产品名称：%s | 产品数量：%s | 产品价格：%s' % (
                    self.goods[i].index, self.goods[i].name, self.goods[i].number, self.goods[i].price))
            if (flag == 0):
                print("库存中没有该产品！！")

    def List_all(self):
        text=''
        n = 0
        c = 0
        for i in range(len(self.goods)):
            n += self.goods[i].number
            c += self.goods[i].number * self.goods[i].price
            text+=('产品ID：%s | 产品名称：%s | 产品数量：%s | 产品价格：%s\n' % (
            self.goods[i].index, self.goods[i].name, self.goods[i].number, self.goods[i].price))
        text+=('-' * 50)
        text += "\n"
        text+=('总计：     |             | 产品总数：%s |产品总价：%s\n' % (n, c))
        return text