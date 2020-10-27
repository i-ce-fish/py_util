import Layout from "@/layout"

const goodtextureRouter = {
    path: "/goodtexture",
    name: "goodtexture",
    redirect: "/goodtexture/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/goodtexture/index"),
        meta: { title: "材质名称管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/goodtexture/edit"),
        hidden: true,
        meta: { title: "修改材质名称" }
    },
    {
        path: "add",
        component: () => import("@/views/goodtexture/add"),
        hidden: true,
        meta: { title: "添加材质名称" }
    }
    ]
}

export default goodtextureRouter