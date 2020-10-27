<template>
    <div class="app-container">
      <el-card>
        <y-form
                ref="supplierorderForm"
                :model="supplierorderForm"
                label-width="80px"
        >

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

          <el-row type="flex" align="space-between">
            <el-col>
                <el-button type="primary" @click="onSearch">查询</el-button>
                <el-button @click="reset" class="y-mr-l-10">重置</el-button>
            </el-col>
            <el-button type="success" @click="add">添加供货商及订货管理</el-button>

          </el-row>
        </y-form>
      </el-card>
        <y-table
            :data="supplierordersData"
            :pagination="pagination"
            @sortBy="sortBy"
            @changePage4List="getList"
            class="y-p-t-20"
        >
            <template>

                
                    
                        <el-table-column prop="supply_source"
                                         label="供货货源"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="joined_at"
                                         label="供应商录入日期"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="supplier_code"
                                         label="供货商编码"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="supply_brand"
                                         label="供货品牌"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="authorized_brand"
                                         label="可授权品牌"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="quality_level"
                                         label="品质档次"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="supply_gender"
                                         label="供货性别"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="supply_series"
                                         label="供货系列"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="supply_category"
                                         label="供货品类"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="supply_age"
                                         label="供货年龄"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="supply_style"
                                         label="供货风格"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="good_memo"
                                         label="货品描述备忘录"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="cost_performance"
                                         label="性价比"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="wholesale_mode"
                                         label="起批方式"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="account_period"
                                         label="账期"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="refundable"
                                         label="能否退货"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="merchant_reliable"
                                         label="商家靠谱程度"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="good_reliable"
                                         label="货品靠谱程度"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                



                <el-table-column label="操作" width="100px"  align="center">
                    <template slot-scope="{row}">
                        <el-button type="text" size="small" @click="edit(row.id)">修改</el-button>
                      <el-divider direction="vertical"></el-divider>
                      <el-button type="text" size="small" @click="del(row.id)">删除</el-button>
                    </template>
                </el-table-column>
            </template>
        </y-table>
    </div>
</template>
<script>
    import {getSupplierorders, delSupplierorder} from "@/api/supplierorder"

    export default {
        data() {
            return {
            supplierorderForm: {},
            supplierordersData: [],
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
                const {data} = await getSupplierorders(
                    {
                        ...param,
                        page: this.pagination.pageNumber,
                        pagesize: this.pagination.pageSize
                    }
                )
                this.supplierordersData = data.list
                this.pagination.total = data.pagination.total
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
                        delSupplierorder(id).then((response) => {
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
                this.getList({...this.supplierorderForm, ...sort})
            },
            sortBy(e) {
                this.onSearch(e)
            },
            reset() {
                this.supplierorderForm = {}
                this.getList()
            }
        }
    }
</script>

<style lang='scss' scoped>
.app-container {

}
</style>