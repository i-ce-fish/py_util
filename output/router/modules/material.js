import Layout from "@/layout"

const materialRouter = {
    path: "/material",
    name: "material",
    redirect: "/material/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/material/index"),
        meta: { title: "材质管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/material/edit"),
        hidden: true,
        meta: { title: "修改材质" }
    },
    {
        path: "add",
        component: () => import("@/views/material/add"),
        hidden: true,
        meta: { title: "添加材质" }
    }
    ]
}

export default materialRouter