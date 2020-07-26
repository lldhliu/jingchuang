"""
 Created by ldh on 18-11-22
"""
from flask import request, render_template, redirect, url_for
from flask_login import current_user, login_required

from app.models.equipment import Equipment
from app.models.equipment_data import EquipmentData

from . import web

__author__ = "ldh"

# # 第二种注册路由方式（使用基于类的视图（即插视图）方式使用）
# app.add_url_rule('/hello', view_func=hello)


@web.route('/equipment', methods=['POST', 'GET'])  # 第一种注册路由方式（一般使用）
@web.route('/equipment/<int:page>')  # 第一种注册路由方式（一般使用）
@login_required
def equipment(page=1):
    if request.method == "POST":
        print(request.form.to_dict())
    if current_user.nickname == "admin":
        equipments = Equipment.get_equ_list(page)
    else:
        equipments = Equipment.get_equ_list(page, current_user.id)

    return render_template('equipment.html', equipments=equipments)


@web.route('/equipment/create', methods=['POST', 'GET'])
@login_required
def equipment_create():
    if request.method == 'POST':
        print(request.form.to_dict())
        return redirect(url_for('web.equipment'))
    return render_template('equipment_create.html')


@web.route('/equipment/data', methods=['POST', 'GET'])
@web.route('/equipment/data/<int:page>')  # 第一种注册路由方式（一般使用）
@login_required
def equipment_data(page=1):
    if request.method == 'POST':
        print(request.form.to_dict())
        return redirect(url_for('web.equipment_data'))
    if current_user.nickname == "admin":
        history_data = EquipmentData.get_data_list(page)
    else:
        print(current_user.id)
        equ_ids = Equipment.get_equ_ids(current_user.id)
        print(equ_ids)
        history_data = EquipmentData.get_data_list(page, equ_ids)
    return render_template('equipment_data.html', history_data=history_data)

