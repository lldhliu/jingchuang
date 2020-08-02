"""
 Created by ldh on 18-11-22
"""
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required

from app.forms.equipment import CreateEquipmentForm, QueryForm
from app.libs.data_utils import get_adverse
from app.libs.enums import EquipmentType
from app.libs.hex_utils import Hex
from app.models.base import db
from app.models.equipment import Equipment
from app.models.humidity import Humidity
from app.models.switch import Switch
from app.models.temperature import Temperature
from app.view_models.equipment import EquipmentCollection
from app.view_models.humidity import HumidityCollection
from app.view_models.switch import SwitchCollection
from app.view_models.temperature import TemperatureCollection
from logs import log_equ
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
    # print(history_data.total)
    return render_template('temperature.html', history_data=history_data)


@web.route('/data/switch', methods=['POST', 'GET'])
@web.route('/data/switch/<int:page>')  # 第一种注册路由方式（一般使用）
@login_required
def switch(page=1):
    form = QueryForm(request.form)
    if request.method == 'POST':
        if form.validate():
            # print(request.form.to_dict())
            # filter_by = request.form.to_dict()['filter_by']
            filter_by = form.filter_by.data
            # filter_content = request.form.to_dict()['filter_content']
            filter_content = form.filter_content.data
            switchs = Switch.get_data_list(page, current_user.is_admin, current_user.id,
                                                     filter_by=filter_by, filter_content=filter_content)
            history_data = SwitchCollection(switchs)
            return render_template('switch.html', history_data=history_data)
        return render_template('switch.html', form=form)

    switchs = Switch.get_data_list(page, current_user.is_admin, current_user.id)
    history_data = SwitchCollection(switchs)
    return render_template('switch.html', history_data=history_data)


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
    temp = Temperature()
    temp.raw_data = raw_data
    log_equ('温度接口数据: ', raw_data)
    return Hex.string_to_hex("ok")


@web.route('/recieve/switch', methods=['POST'])
def recieve_switch():
    print(request.form.to_dict())
    raw_data = request.form.to_dict()
    switch = Switch()
    switch.raw_data = raw_data
    log_equ('合模次数接口数据: ', raw_data)
    return Hex.string_to_hex("ok")


@web.route('/recieve/humidity', methods=['POST'])
def recieve_humidity():
    print(request.form.to_dict())
    raw_data = request.form.to_dict()
    humidity = Humidity()
    humidity.raw_data = raw_data
    log_equ('湿度接口数据: ', raw_data)
    return Hex.string_to_hex("ok")


@web.route('/data/recieve', methods=['POST'])
def recieve_data():
    print(request.form.to_dict())
    raw_data = request.form.to_dict()
    log_equ('data接口数据: ', raw_data)

    cm_no = raw_data['cmid']
    # print(cm_no)
    equ = Equipment.get_equ_by_cmid(cm_no)
    if not equ:
        # print('error equ no')
        return '404'
    data_list = raw_data['data'].split('2255')
    switch_data = data_list[0]
    add_switch = add_switch_data(switch_data, equ)

    humidity_data = data_list[1]
    add_humidity = add_shumidity_data(humidity_data, equ)

    temp_data = data_list[2]
    add_temp = add_temperature_data(temp_data, equ)

    # return Hex.string_to_hex("ok")
    if add_switch and add_humidity and add_temp:
        return '200'
    else:
        return '404'


def add_switch_data(switch_data, equ):
    with db.auto_commit():
        switch = Switch()
        switch.switch = int(switch_data, 16)
        switch.equ_id = equ.id
        switch.raw_data = switch_data
        last_switch = Switch.get_last_data(equ.id)
        if not last_switch:
            # print('no switch data')
            switch.count = 1
            equ.open_count = 1
            db.session.add(switch)
            db.session.add(equ)
        else:
            # print(switch_data)
            if switch_data == '00':
                switch.count = last_switch.count + 1
                equ.open_count = last_switch.count + 1
                db.session.add(switch)
                db.session.add(equ)
            elif switch_data == '01':
                switch.count = last_switch.count
                db.session.add(switch)

    return True


def add_shumidity_data(humidity_data, equ):
    with db.auto_commit():
        humidity = Humidity()
        humidity.raw_data = humidity_data
        if len(humidity_data) != 18:
            return False
        hex_h = humidity_data[10: 14]
        if hex_h == '8000':
            humidity.humidity = None
            equ.humidity = None
        else:
            humidity.equ_id = equ.id

            bin_h = bin(int(hex_h, 16)).replace('0b', '')
            # print(int(bin_i, 16))
            if len(bin_h) == 16 and bin_h[0] == '1':
                # print(Hex.Getadverse(a))
                h = get_adverse(bin_h)
                h = ~int(h, 2) / 10
            else:
                h = int(bin_h, 2) / 10
            humidity.humidity = h
            equ.humidity = h
        db.session.add(humidity)
        db.session.add(equ)


def add_temperature_data(temp_data, equ):
    with db.auto_commit():
        temp = Temperature()
        temp.raw_data = temp_data
        temp.equ_id = equ.id
        if len(temp_data) != 42:
            return False

        t = temp_data[6: 38]
        res = []
        for i in range(8):
            bin_i = t[i*4: i*4+4]
            a = bin(int(bin_i, 16)).replace('0b', '')
            # print(int(bin_i, 16))
            if bin_i == '8000':
                res.append(None)
            elif len(a) == 16 and a[0] == '1':
                # print(Hex.Getadverse(a))
                a = get_adverse(a)
                res.append(~int(a, 2)/10)
            else:
                res.append(int(bin_i, 16)/10)
        temp.mm_temp_01 = res[0]
        temp.mm_temp_02 = res[1]
        temp.mm_temp_03 = res[2]
        temp.mm_temp_04 = res[3]
        temp.fm_temp_01 = res[4]
        temp.fm_temp_02 = res[5]
        temp.fm_temp_03 = res[6]
        temp.fm_temp_04 = res[7]

        equ.mm_temp_01 = res[0]
        equ.mm_temp_02 = res[1]
        equ.mm_temp_03 = res[2]
        equ.mm_temp_04 = res[3]
        equ.fm_temp_01 = res[4]
        equ.fm_temp_02 = res[5]
        equ.fm_temp_03 = res[6]
        equ.fm_temp_04 = res[7]

        db.session.add(temp)
        db.session.add(equ)

    return True
