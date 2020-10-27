import Layout from "@/layout"

const supplierorderRouter = {
    path: "/supplierorder",
    name: "supplierorder",
    redirect: "/supplierorder/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/supplierorder/index"),
        meta: { title: "供货商及订货管理管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/supplierorder/edit"),
        hidden: true,
        meta: { title: "修改供货商及订货管理" }
    },
    {
        path: "add",
        component: () => import("@/views/supplierorder/add"),
        hidden: true,
        meta: { title: "添加供货商及订货管理" }
    }
    ]
}

export default supplierorderRouter