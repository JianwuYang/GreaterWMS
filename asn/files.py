from rest_framework_csv.renderers import CSVStreamingRenderer


def list_file_headers():
    return [
        "asn_code",
        "asn_status",
        # 'total_weight',
        # 'total_volume',
        "total_cost",
        "supplier",
        "creater",
        "create_time",
        "update_time",
    ]


def list_cn_data_header():
    return dict(
        [
            ("asn_code", "ASN单号"),
            ("asn_status", "ASN状态"),
            # ('total_weight', u'总重量'),
            # ('total_volume', u'总体积'),
            ("total_cost", "总成本"),
            ("supplier", "供应商"),
            ("creater", "创建人"),
            ("create_time", "创建时间"),
            ("update_time", "更新时间"),
        ]
    )


def list_en_data_header():
    return dict(
        [
            ("asn_code", "ASN Code"),
            ("asn_status", "ASN Status"),
            # ('total_weight', u'Total Weight'),
            # ('total_volume', u'Total Volume'),
            ("total_cost", "Total Cost"),
            ("supplier", "Supplier"),
            ("creater", "Creater"),
            ("create_time", "Create Time"),
            ("update_time", "Update Time"),
        ]
    )


def detail_file_headers():
    return [
        "asn_code",
        "asn_status",
        "supplier",
        "goods_code",
        "goods_desc",
        "goods_qty",
        "goods_actual_qty",
        "sorted_qty",
        "goods_shortage_qty",
        "goods_more_qty",
        "goods_damage_qty",
        # 'goods_weight',
        # 'goods_volume',
        "goods_cost",
        "creater",
        "create_time",
        "update_time",
    ]


def detail_cn_data_header():
    return dict(
        [
            ("asn_code", "ASN单号"),
            ("asn_status", "ASN状态"),
            ("supplier", "供应商"),
            ("goods_code", "商品编码"),
            ("goods_desc", "商品描述"),
            ("goods_qty", "订单数量"),
            ("goods_actual_qty", "实际到货数量"),
            ("sorted_qty", "已分拣数量"),
            ("goods_shortage_qty", "少到货数量"),
            ("goods_more_qty", "多到货数量"),
            ("goods_damage_qty", "破损数量"),
            # ('goods_weight', u'商品重量'),
            # ('goods_volume', u'商品体积'),
            ("goods_cost", "商品成本"),
            ("creater", "创建人"),
            ("create_time", "创建时间"),
            ("update_time", "更新时间"),
        ]
    )


def detail_en_data_header():
    return dict(
        [
            ("asn_code", "ASN Code"),
            ("asn_status", "ASN Status"),
            ("supplier", "Supplier"),
            ("goods_code", "Goods Code"),
            ("goods_desc", "Goods Description"),
            ("goods_qty", "Goods Qty"),
            ("goods_actual_qty", "Goods Actual Qty"),
            ("sorted_qty", "Sorted Qty"),
            ("goods_shortage_qty", "Goods Shortage Qty"),
            ("goods_more_qty", "Goods More Qty"),
            ("goods_damage_qty", "Goods Damage Qty"),
            # ('goods_weight', u'Goods Weight'),
            # ('goods_volume', u'Goods Volume'),
            ("goods_cost", "Goods Cost"),
            ("creater", "Creater"),
            ("create_time", "Create Time"),
            ("update_time", "Update Time"),
        ]
    )


class FileListRenderCN(CSVStreamingRenderer):
    header = list_file_headers()
    labels = list_cn_data_header()


class FileListRenderEN(CSVStreamingRenderer):
    header = list_file_headers()
    labels = list_en_data_header()


class FileDetailRenderCN(CSVStreamingRenderer):
    header = detail_file_headers()
    labels = detail_cn_data_header()


class FileDetailRenderEN(CSVStreamingRenderer):
    header = detail_file_headers()
    labels = detail_en_data_header()
