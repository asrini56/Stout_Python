#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 02:39:13 2021

@author: ashwins
"""

import csv


def parseCustomerOrder():
    f = open('/Users/srini/PycharmProjects/Density Est and Classification/casestudy.csv', 'r')
    dataset = csv.reader(f)
    revenue_map = {}
    customer_map = {}
    new_customer_map = {}
    new_customer_revenue_map = {}
    old_customer_map = {}
    old_customer_curr_revenue_map = {}
    old_customer_growth_map = {}
    lost_customer_map = {}

    i = 0
    for row in dataset:
        if i > 0:
            revenue_map[row[3]] = revenue_map.get(row[3], 0) + float(row[2])
            c = customer_map.get(row[3], set())
            c.add(row[1].strip())
            customer_map[row[3]] = c
            prev = str(int(row[3]) - 1)
            if prev in customer_map:
                if row[1].strip() not in customer_map[prev]:
                    n_c = new_customer_map.get(row[3], set())
                    n_c.add(row[1].strip())
                    new_customer_map[row[3]] = n_c
                    '''n_r = new_customer_revenue_map.get(row[3], set())
                    n_r.add(float(row[2]))
                    new_customer_revenue_map[row[3]] = n_r'''
                    new_customer_revenue_map[row[3]] = new_customer_revenue_map.get(row[3], 0) + (float(row[2]))
                else:
                    o_c = old_customer_map.get(row[3], set())
                    o_c.add(row[1].strip())
                    old_customer_map[row[3]] = o_c
                    '''o_r = old_customer_curr_revenue_map.get(row[3], set())
                    o_r.add(float(row[2]))
                    old_customer_curr_revenue_map[row[3]] = o_r'''
                    old_customer_curr_revenue_map[row[3]] = old_customer_curr_revenue_map.get(row[3], 0) + (float(row[2]))
        i += 1
    for year in customer_map:
        next_yr = str(int(year) + 1)
        if next_yr in customer_map:
            for c in customer_map[year]:
                if c not in customer_map[next_yr]:
                    l_c = lost_customer_map.get(next_yr, set())
                    l_c.add(c)
                    lost_customer_map[next_yr] = l_c

    total_customer = dict({x: len(customer_map[x]) for x in customer_map})
    no_of_new_customer = dict({x: len(new_customer_map[x]) for x in new_customer_map})
    no_of_old_customer = dict({x: len(old_customer_map[x]) for x in old_customer_map})
    # 1. Total revenue for the current year
    print(revenue_map)
    # 2. New Customer Revenue
    print(new_customer_revenue_map)
    # 5. Existing Customer Revenue Current Year
    print(old_customer_curr_revenue_map)
    # 7. & 8. Total Customers Current and Previous Year
    print(total_customer)
    # 9. New Customers
    print(no_of_new_customer)
    # 10. Old Customers
    print(no_of_old_customer)


parseCustomerOrder()