<template>
    <div class="app-container">
        <y-form
                ref="goodForm"
                :model="goodForm"
                label-width="80px"
        >
            <el-row type="flex" justify="end">
                <el-form-item>
                    <el-button type="success" @click="add">添加商品模块</el-button>
                </el-form-item>
            </el-row>


            
            
            
            <el-row type="flex" justify="space-between">
                <el-col :span="20">
                    <el-row>

                        
                        
                        <el-col :span="6">
                            <el-form-item label="商品名称:" prop="product_name">

                                
                                
                                <y-input
                                
                                v-model="goodForm.product_name"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="商品编号:" prop="product_sn">

                                
                                
                                <y-input
                                
                                v-model="goodForm.product_sn"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="款式编号:" prop="type_sn">

                                
                                
                                <y-input
                                
                                v-model="goodForm.type_sn"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="适合性别:" prop="gender">

                                
                                
                                <y-select
                                
                                v-model="goodForm.gender"
                                
                                
                                
                                
                                
                                  :options="[{value: '1',label: '男'},{value: '0',label: '女'}]"  

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="材质:" prop="material">

                                
                                
                                <y-input
                                
                                v-model="goodForm.material"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="吊牌价格:" prop="original_price">

                                
                                
                                <y-input
                                
                                v-model="goodForm.original_price"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="优惠价格:" prop="onsale_price">

                                
                                
                                <y-input
                                
                                v-model="goodForm.onsale_price"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="vip价格:" prop="vip_price">

                                
                                
                                <y-input
                                
                                v-model="goodForm.vip_price"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="颜色:" prop="colors">

                                
                                
                                <y-input
                                
                                v-model="goodForm.colors"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="尺码:" prop="sizes">

                                
                                
                                <y-input
                                
                                v-model="goodForm.sizes"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        

                    </el-row>
                </el-col>
                <el-col :span="4">
                    <el-row type="flex" justify="end">
                        <el-form-item>
                            <el-button type="primary" @click="onSearch">查询</el-button>
                            <el-button @click="reset" class="no-margin">重置</el-button>
                        </el-form-item>
                    </el-row>
                </el-col>
            </el-row>
            

        </y-form>

        <y-table :data="goodsData" :pagination="pagination" @sortBy="sortBy" @changePage4List="getList">
            <template>

                
                    
                        <el-table-column prop="product_name" label="商品名称"
                                          sortable="product_name" 
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="product_sn" label="商品编号"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="type_sn" label="款式编号"
                                          sortable="type_sn" 
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="gender" label="适合性别"
                                          sortable="gender" 
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="material" label="材质"
                                          sortable="material" 
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="original_price" label="吊牌价格"
                                          sortable="original_price" 
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="onsale_price" label="优惠价格"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="vip_price" label="vip价格"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="colors" label="颜色"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="sizes" label="尺码"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                
                    
                
                    
                
                    
                



                <el-table-column label="操作" width="100px">
                    <template slot-scope="{row}">
                        <el-button type="text" size="small" @click="edit(row.id)">修改</el-button>
                        <el-button type="text" size="small" @click="del(row.id)">删除</el-button>
                    </template>
                </el-table-column>
            </template>
        </y-table>
    </div>
</template>
<script>
    import {getGoods, delGood} from "@/api/good"

    export default {
        data() {
            return {
            goodForm: {},
            goodsData: [],
                pagination: {
                pageNumber: 1,
                    pageSize: 10
            },
            
        }
        },
        created() {
            this.getList()
        },
        methods: {
            async getList(param) {
                const response = await getGoods(
                    {
                        ...param,
                        page: this.pagination.pageNumber,
                        pagesize: this.pagination.pageSize
                    }
                )
                this.goodsData = response.data.list
                this.pagination.total = parseInt(response.data.pagination.total, 10)
            },

            add() {
                this.$router.push({path: "add"})
            },
            edit(id) {
                this.$router.push({path: "edit", query: {id}})
            },
            del(id) {
                this.$confirm("是否删除?", "提示", {
                    confirmButtonText: "确定",
                    cancelButtonText: "取消",
                    type: "warning"
                })
                    .then(() => {
                        delGood(id).then((response) => {
                            this.$message({
                                type: "success",
                                message: "删除成功!"
                            })
                            this.getList()
                        })
                    })
                    .catch(() => {
                        this.$message({
                            type: "info",
                            message: "已取消删除"
                        })
                    })
            },
            onSearch(sort) {
                this.getList({...this.goodForm, ...sort})
            },
            sortBy(e) {
                this.onSearch(e)
            },
            reset() {
                this.goodForm = {}
                this.getList()
            }
        }
    }
</script>

<style lang='scss' scope>
    .app-container {
        padding: 20px;
        .no-margin{
            margin: 0;
        }
    }
</style>