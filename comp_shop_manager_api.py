from flask import Flask, request
from cpu import Cpu
from gpu import Gpu
from comp_shop_manager import ComputerShopManager
import json
from datetime import datetime

app = Flask(__name__)

comp_shop = ComputerShopManager('bryanshop.sqlite')


@app.route('/compshop/parts', methods=['POST'])
def add_part():
    """ Adds a part to shop manager """
    content = request.json
    if content["type"] == "CPU":
        try:
            cpu = Cpu(content['clock_speed_ghz'],
                      content['boost_clock_ghz'],
                      content['core_count'],
                      content['socket'],
                      content['hyperthread'],
                      content['model'],
                      content['manufacturer'],
                      content['price'],
                      content['cost'],
                      content['stock'],
                      content["release_date"])
            comp_shop.add_part(cpu)
            response = app.response_class(
                status=200
            )
        except ValueError as e:
            response = app.response_class(
                response=str(e),
                status=400
            )
        return response
    elif content['type'] == "GPU":
        try:
            gpu = Gpu(content['clock_speed_mhz'],
                      content['boost_clock_mhz'],
                      content['chipset'],
                      content['pcie_ver'],
                      content['length_cm'],
                      content['thickness_cm'],
                      content['model'],
                      content['manufacturer'],
                      content['price'],
                      content['cost'],
                      content['stock'],
                      content["release_date"])
            comp_shop.add_part(gpu)
            response = app.response_class(
                status=200
            )
        except ValueError as e:
            response = app.response_class(
                response=str(e),
                status=400
            )
        return response


@app.route('/compshop/parts/<string:model>', methods=['GET'])
def get_part_by_model(model):
    """ Get an existing device in the manager """
    try:
        part = comp_shop.get_part_by_model(model)
        if part is None:
            raise ValueError("No Part Exist with this Model")
        response = app.response_class(
            status=200,
            response=json.dumps(part.to_dict()),
            mimetype='application/json'
        )
        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response


@app.route('/compshop/parts/update', methods=['PUT'])
def update():
    """Replace a part in the inventory based on model"""
    content = request.json
    try:
        part = {}
        part['model'] = content['model']
        part['stock'] = content['stock']
        part['is_discontinued'] = content["is_discontinued"]
        comp_shop.update(part)
        response = app.response_class(
            status=200
        )
        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response


@app.route('/compshop/parts/<string:model>', methods=['DELETE'])
def delete_by_model(model):
    """ Delete an existing device in the manager """
    try:
        part = comp_shop.delete_by_model(model)
        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response


@app.route('/compshop/shopstats', methods=['GET'])
def get_shop_stats():
    """ Get Shop Stats for the Shop Manager """
    try:
        stats = comp_shop.get_shop_stats()
        response = app.response_class(
            status=200,
            response=json.dumps(stats.to_dict()),
            mimetype='application/json'
        )
        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response


@app.route('/compshop/parts/all/<type>', methods=['GET'])
def get_all_by_type(type):
    """ Get All parts description of the selected type in the shop manager """
    try:
        type_upper = type.upper()
        all_part_type = comp_shop.get_all_by_type(type_upper)
        part_list = []
        for part in all_part_type:
            part_list.append(part.get_description())
        response = app.response_class(
            status=200,
            response=json.dumps(part_list),
            mimetype='application/json'
        )
        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response


@app.route('/compshop/parts/all', methods=['GET'])
def get_all_parts():
    """ Get all parts """
    try:
        all_part = comp_shop.get_all()
        part_list = []
        for part in all_part:
            part_list.append(part.to_dict())
        response = app.response_class(
            status=200,
            response=json.dumps(part_list),
            mimetype='application/json'
        )
        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response


if __name__ == "__main__":
    app.run()

