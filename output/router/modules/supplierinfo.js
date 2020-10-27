import Layout from "@/layout"

const supplierinfoRouter = {
    path: "/supplierinfo",
    name: "supplierinfo",
    redirect: "/supplierinfo/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/supplierinfo/index"),
        meta: { title: "供货商及订货管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/supplierinfo/edit"),
        hidden: true,
        meta: { title: "修改供货商及订货" }
    },
    {
        path: "add",
        component: () => import("@/views/supplierinfo/add"),
        hidden: true,
        meta: { title: "添加供货商及订货" }
    }
    ]
}

export default supplierinfoRouter