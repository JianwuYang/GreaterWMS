from rest_framework_csv.renderers import CSVStreamingRenderer


def list_file_headers():
    return [
        "dn_code",
        "dn_status",
        # 'total_weight',
        # 'total_volume',
        "customer",
        "creater",
        "back_order_label",
        "create_time",
        "update_time",
    ]


def list_cn_data_header():
    return dict(
        [
            ("dn_code", "发货单单号"),
            ("dn_status", "发货单状态"),
            # ('total_weight', u'总重量'),
            # ('total_volume', u'总体积'),
            ("customer", "客户"),
            ("creater", "创建人"),
            ("back_order_label", "欠货订单标识"),
            ("create_time", "创建时间"),
            ("update_time", "更新时间"),
        ]
    )


def list_en_data_header():
    return dict(
        [
            ("dn_code", "DN Code"),
            ("dn_status", "DN Status"),
            # ('total_weight', u'Total Weight'),
            # ('total_volume', u'Total Volume'),
            ("customer", "Customer"),
            ("creater", "Creater"),
            ("back_order_label", "Back Order Label"),
            ("create_time", "Create Time"),
            ("update_time", "Update Time"),
        ]
    )


def detail_file_headers():
    return [
        "dn_code",
        "dn_status",
        "goods_code",
        "goods_desc",
        "goods_qty",
        "pick_qty",
        "picked_qty",
        "intransit_qty",
        "delivery_actual_qty",
        "delivery_shortage_qty",
        "delivery_more_qty",
        "delivery_damage_qty",
        # 'goods_weight',
        # 'goods_volume',
        "customer",
        "creater",
        "back_order_label",
        "create_time",
        "update_time",
    ]


def detail_cn_data_header():
    return dict(
        [
            ("dn_code", "发货单单号"),
            ("dn_status", "发货单状态"),
            ("goods_code", "发货单货物名称"),
            ("goods_desc", "发货单货物描述"),
            ("goods_qty", "发货单数量"),
            ("pick_qty", "需要拣货数量"),
            ("picked_qty", "已拣货数量"),
            ("intransit_qty", "在途库存"),
            ("delivery_actual_qty", "实际到货"),
            ("delivery_shortage_qty", "到货短少"),
            ("delivery_more_qty", "多到货"),
            ("delivery_damage_qty", "到货破损"),
            # ('goods_weight', u'商品重量'),
            # ('goods_volume', u'商品体积'),
            ("customer", "客户"),
            ("creater", "创建人"),
            ("back_order_label", "欠货订单标识"),
            ("create_time", "创建时间"),
            ("update_time", "更新时间"),
        ]
    )


def detail_en_data_header():
    return dict(
        [
            ("dn_code", "DN Code"),
            ("dn_status", "DN Status"),
            ("goods_code", "Goods Code"),
            ("goods_desc", "Goods Description"),
            ("goods_qty", "Goods Qty"),
            ("pick_qty", "Pick Qty"),
            ("picked_qty", "Picked Qty"),
            ("intransit_qty", "Intransit Qty"),
            ("delivery_actual_qty", "Delivery Actual Qty"),
            ("delivery_shortage_qty", "Delivery Shortage Qty"),
            ("delivery_more_qty", "Delivery More Qty"),
            ("delivery_damage_qty", "Delivery Damage Qty"),
            # ('goods_weight', u'Goods Weight'),
            # ('goods_volume', u'Goods Volume'),
            ("customer", "Customer"),
            ("creater", "Creater"),
            ("back_order_label", "Back Order Label"),
            ("create_time", "Create Time"),
            ("update_time", "Update Time"),
        ]
    )


class FileListRenderCN(CSVStreamingRenderer):
    header = list_file_headers()
    labels = list_cn_data_header()


class FileListRenderEN(CSVStreamingRenderer):
    header = list_file_headers()
    labels = list_cn_data_header()


class FileDetailRenderCN(CSVStreamingRenderer):
    header = detail_file_headers()
    labels = detail_cn_data_header()


class FileDetailRenderEN(CSVStreamingRenderer):
    header = detail_file_headers()
    labels = detail_en_data_header()
