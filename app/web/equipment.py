"""
 Created by ldh on 18-11-22
"""
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required

from app.forms.equipment import CreateEquipmentForm, QueryForm
from app.libs.enums import EquipmentType
from app.models.base import db
from app.models.equipment import Equipment
from app.models.humidity import Humidity
from app.models.swich import Swich
from app.models.temperature import Temperature
from app.view_models.equipment import EquipmentCollection
from app.view_models.humidity import HumidityCollection
from app.view_models.swich import SwichCollection
from app.view_models.temperature import TemperatureCollection
from . import web

__author__ = "ldh"

# # 第二种注册路由方式（使用基于类的视图（即插视图）方式使用）
# app.add_url_rule('/hello', view_func=hello)


@web.route('/equipment', methods=['POST', 'GET'])  # 第一种注册路由方式（一般使用）
@web.route('/equipment/<int:page>')  # 第一种注册路由方式（一般使用）
@login_required
def equipment(page=1):
    form = QueryForm(request.form)
    if request.method == 'POST':
        if form.validate():
            # print(request.form.to_dict())
            filter_by = form.filter_by.data
            filter_content = form.filter_content.data
            equipments = Equipment.get_equ_list(page, current_user.is_admin, current_user.id,
                                                filter_by=filter_by, filter_content=filter_content)
            equipments = EquipmentCollection(equipments)
            if equipments.total:
                return render_template('equipment.html', equipments=equipments)
            else:
                flash("未查询到指定结果")
                return render_template('equipment.html', equipments=equipments)
        return render_template('equipment.html', form=form)

    equipments = Equipment.get_equ_list(page, current_user.is_admin, current_user.id)
    equipments = EquipmentCollection(equipments)
    if equipments.total:
        return render_template('equipment.html', equipments=equipments)
    else:
        flash("还没有任何设备, 请点击新增设备来添加你的设备吧！")
        return render_template('equipment.html', equipments=equipments)


@web.route('/create', methods=['POST', 'GET'])
@login_required
def equipment_create():
    print(request.form.to_dict())
    form = CreateEquipmentForm(request.form)
    # print(form.validate())
    if request.method == 'POST':
        if form.validate():
            with db.auto_commit():
                equipment = Equipment()
                equipment.set_attrs(form.data)
                equipment.uid = current_user.id
                equipment.type = EquipmentType[request.form.to_dict()['type']]
                equipment.create_by = current_user.nickname
                db.session.add(equipment)
            # print(request.form.to_dict())
            return redirect(url_for('web.equipment'))

        return render_template('equipment_create.html', form=form)

    return render_template('equipment_create.html')


@web.route('/data/temperature', methods=['POST', 'GET'])
@web.route('/data/temperature/<int:page>')  # 第一种注册路由方式（一般使用）
@login_required
def temperature(page=1):
    form = QueryForm(request.form)
    if request.method == 'POST':
        if form.validate():
            # print(request.form.to_dict())
            # filter_by = request.form.to_dict()['filter_by']
            filter_by = form.filter_by.data
            # filter_content = request.form.to_dict()['filter_content']
            filter_content = form.filter_content.data
            temperatures = Temperature.get_data_list(page, current_user.is_admin, current_user.id,
                                                      filter_by=filter_by, filter_content=filter_content)
            history_data = TemperatureCollection(temperatures)
            return render_template('temperature.html', history_data=history_data)
        return render_template('temperature.html', form=form)

    temperatures = Temperature.get_data_list(page, current_user.is_admin, current_user.id)
    history_data = TemperatureCollection(temperatures)
    return render_template('temperature.html', history_data=history_data)


@web.route('/data/swich', methods=['POST', 'GET'])
@web.route('/data/swich/<int:page>')  # 第一种注册路由方式（一般使用）
@login_required
def swich(page=1):
    form = QueryForm(request.form)
    if request.method == 'POST':
        if form.validate():
            # print(request.form.to_dict())
            # filter_by = request.form.to_dict()['filter_by']
            filter_by = form.filter_by.data
            # filter_content = request.form.to_dict()['filter_content']
            filter_content = form.filter_content.data
            swichs = Swich.get_data_list(page, current_user.is_admin, current_user.id,
                                                     filter_by=filter_by, filter_content=filter_content)
            history_data = SwichCollection(swichs)
            return render_template('swich.html', history_data=history_data)
        return render_template('swich.html', form=form)

    swichs = Swich.get_data_list(page, current_user.is_admin, current_user.id)
    history_data = SwichCollection(swichs)
    return render_template('swich.html', history_data=history_data)


@web.route('/data/humidity', methods=['POST', 'GET'])
@web.route('/data/humidity/<int:page>')  # 第一种注册路由方式（一般使用）
@login_required
def humidity(page=1):
    form = QueryForm(request.form)
    if request.method == 'POST':
        if form.validate():
            # print(request.form.to_dict())
            # filter_by = request.form.to_dict()['filter_by']
            filter_by = form.filter_by.data
            # filter_content = request.form.to_dict()['filter_content']
            filter_content = form.filter_content.data
            humidities = Humidity.get_data_list(page, current_user.is_admin, current_user.id,
                                                     filter_by=filter_by, filter_content=filter_content)
            history_data = HumidityCollection(humidities)
            return render_template('humidity.html', history_data=history_data)
        return render_template('humidity.html', form=form)

    humidities = Humidity.get_data_list(page, current_user.is_admin, current_user.id)
    history_data = HumidityCollection(humidities)
    return render_template('humidity.html', history_data=history_data)


@web.route('/recieve/temperature', methods=['POST'])
def recieve_temperature():
    print(request.form.to_dict())
    raw_data = request.form.to_dict()
    return 'ok'


@web.route('/recieve/switch', methods=['POST'])
def recieve_switch():
    print(request.form.to_dict())
    raw_data = request.form.to_dict()
    return 'ok'
